//Diccionario para mapear los tipos de eventos a títulos amigables.
const tipoEventosMap = {
    "inicio_semestre": "Inicio de Semestre",
    "fin_semestre": "Fin de Semestre",
    "inicio_inscripcion": "Inicio de Inscripción de Asignaturas",
    "fin_inscripcion": "Fin de Inscripción de Asignaturas",
    "receso": "Receso Académico",
    "feriado_nacional": "Feriado Nacional",
    "feriado_regional": "Feriado Regional",
    "inicio_solicitudes": "Inicio de Plazos de Solicitudes Administrativas",
    "fin_solicitudes": "Fin de Plazos de Solicitudes Administrativas",
    "inicio_beneficios": "Inicio de Plazos para la Gestión de Beneficios",
    "fin_beneficios": "Fin de Plazos para la Gestión de Beneficios",
    "ceremonia_titulacion": "Ceremonia de Titulación o Graduación",
    "reunion_consejo": "Reunión de Consejo Académico",
    "taller_charla": "Talleres y Charlas",
    "orientacion": "Día de Orientación para Nuevos Estudiantes",
    "extracurricular": "Eventos Extracurriculares",
    "inicio_clases": "Inicio de Clases",
    "ultimo_dia_clases": "Último Día de Clases",
    "puertas_abiertas": "Día de Puertas Abiertas",
    "suspension_completa": "Suspensión de Actividades Completa",
    "suspension_parcial": "Suspensión de Actividades Parcial"
};

document.addEventListener("DOMContentLoaded", async function () {

    var calendarEl = document.getElementById("calendar");
    var filterSelect = document.getElementById("filter-select");

    //Crear elementos para el cuadro de diálogo.
    const dialogOverlay = document.createElement("div");
    const dialog = document.createElement("div");
    const dialogTitle = document.createElement("h3");
    const dialogEvent = document.createElement("p");
    const dialogDescription = document.createElement("p");
    const closeButton = document.createElement("button");

    //Estilos e identificadores para el cuadro de diálogo.
    dialogOverlay.id = "dialog-overlay";
    dialog.classList.add("dialog");
    closeButton.textContent = "Cerrar";

    //Añadir elementos al cuadro de diálogo.
    dialog.appendChild(dialogTitle);
    dialog.appendChild(dialogEvent);
    dialog.appendChild(dialogDescription);
    dialog.appendChild(closeButton);
    document.body.appendChild(dialogOverlay);
    document.body.appendChild(dialog);

    //Cargar datos desde la API.
    const calendarioData = await (await fetch("http://127.0.0.1:8000/api/calendario/")).json();

    //Procesar feriados nacionales.
    var feriados = calendarioData.feriados.map(feriado => ({
        id: "feriado_nacional",                       //ID genérico para feriados nacionales.
        type: "Feriado Nacional",                     //Tipo amigable.
        title: feriado.nombre,                        //Título mostrado en el calendario.
        originalTitle: feriado.nombre,                //Título original del feriado.
        start: feriado.fecha,                         //Fecha del feriado.
        color: "green",                               //Color para feriados nacionales.
        allDay: true                                  //Feriados ocupan todo el día.
    }));

    //Procesar eventos académicos.
    var eventos = calendarioData.eventos.map(evento => {
        const tipoAmigable = tipoEventosMap[evento.tipo] || "Otro"; 
        return {
            id: evento.tipo,                                              //Tipo del evento.
            type: tipoAmigable,                                           //Tipo amigable.
            title: `${tipoAmigable}: ${evento.titulo}`,                   //Título mostrado en el calendario.
            originalTitle: evento.titulo,                                 //Título original del evento.
            start: evento.fecha_inicio,                                   //Fecha de inicio del evento.
            end: evento.fecha_fin,                                        //Fecha de fin del evento.
            description: evento.descripcion,                              //Descripción del evento.
            color: "blue"
        };
    });

    //Combinar feriados y eventos en una lista única.
    var allEvents = [...feriados, ...eventos];

    //Inicializar el calendario con todos los eventos.
    var calendar = new FullCalendar.Calendar(calendarEl, {
        locale: "es",
        initialView: "dayGridMonth",
        events: allEvents,
        headerToolbar: {
            left: "prev,next,today", // Botones a la izquierda.
            center: "title", // El título se centra.
            right: "dayGridMonth,timeGridWeek,timeGridDay" // Botones a la derecha.
        },
        titleFormat: { // Personalización del formato del título.
            year: "numeric", // Muestra el año completo.
            month: "long" // Muestra el nombre completo del mes.
        },
        eventClick: function (info) {

            const tipo = info.event.extendedProps.type || "Otro";                          //Tipo del evento.
            const titulo = info.event.extendedProps.originalTitle || info.event.title;     //Título original.
            const descripcion = info.event.extendedProps.description || "Sin descripción."; //Descripción.

            dialogTitle.textContent = tipo;                                //Encabezado del cuadro de diálogo.
            dialogEvent.textContent = `Evento: ${titulo}`;                 //Título del evento.
            dialogDescription.textContent = `Descripción: ${descripcion}`; //Descripción del evento.
            dialogOverlay.style.display = "block";                         //Mostrar el fondo oscuro.
            dialog.style.display = "flex";                                 //Mostrar el cuadro de diálogo.
        }
    });
    

    //Renderizar el calendario.
    calendar.render();


    //Cerrar el cuadro de diálogo al hacer clic en el botón.
    closeButton.addEventListener("click", function () {
        dialogOverlay.style.display = "none";
        dialog.style.display = "none";
    });

    //Obtener categorías únicas (Feriado Nacional + tipos de eventos académicos).
    const categoriasUnicas = ["Feriado Nacional", ...new Set(eventos.map(evento => evento.type))];

    //Rellenar el combobox con las categorías.
    categoriasUnicas.forEach(categoria => {
        const option = document.createElement("option"); //Crear opción.
        option.value = categoria;                        //Valor de la opción.
        option.textContent = categoria;                  //Texto mostrado.
        filterSelect.appendChild(option);                //Añadir opción al select.
    });

    //Filtrar eventos según la categoría seleccionada.
    filterSelect.addEventListener("change", function () {
        const filter = this.value;
        const filteredEvents = allEvents.filter(evento => {
            return filter === "all" || evento.type === filter;
        });

        //Eliminar eventos actuales y agrega los eventos filtrados.
        calendar.removeAllEvents();
        calendar.addEventSource(filteredEvents);
    });
});
