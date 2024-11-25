// Diccionario para mapear los tipos de eventos a títulos amigables
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

    // Crear elementos del cuadro de diálogo
    const dialogOverlay = document.createElement("div");
    const dialog = document.createElement("div");
    const dialogTitle = document.createElement("h3");
    const dialogEvent = document.createElement("p");
    const dialogDescription = document.createElement("p");
    const closeButton = document.createElement("button");

    dialogOverlay.id = "dialog-overlay";
    dialog.classList.add("dialog");
    closeButton.textContent = "Cerrar";

    // Añadir elementos al diálogo
    dialog.appendChild(dialogTitle);
    dialog.appendChild(dialogEvent);
    dialog.appendChild(dialogDescription);
    dialog.appendChild(closeButton);
    document.body.appendChild(dialogOverlay);
    document.body.appendChild(dialog);

    // Cargar datos desde la API
    const calendarioData = await (await fetch("http://127.0.0.1:8000/api/calendario/")).json();

    // Procesar feriados nacionales
    var feriados = calendarioData.feriados.map(feriado => ({
        id: "feriado_nacional",
        type: "Feriado Nacional",
        title: `Feriado Nacional: ${feriado.nombre}`, // Título combinado
        originalTitle: feriado.nombre, // Título original
        start: feriado.fecha,
        color: "green",
        allDay: true
    }));

    // Procesar eventos académicos
    var eventos = calendarioData.eventos.map(evento => {
        const tipoAmigable = tipoEventosMap[evento.tipo] || "Otro";
        return {
            id: evento.tipo,
            type: tipoAmigable, // Tipo amigable
            title: `${tipoAmigable}: ${evento.titulo}`, // Título combinado
            originalTitle: evento.titulo, // Título original
            start: evento.fecha_inicio,
            end: evento.fecha_fin,
            description: evento.descripcion,
            color: evento.tipo === "suspension_completa" ? "red" : "blue"
        };
    });

    // Combinar todos los eventos
    var allEvents = [...feriados, ...eventos];

    // Inicializar el calendario con todos los eventos
    var calendar = new FullCalendar.Calendar(calendarEl, {
        locale: "es",
        initialView: "dayGridMonth",
        events: allEvents,
        eventClick: function (info) {
            // Mostrar el cuadro de diálogo con los detalles del evento
            const tipo = info.event.extendedProps.type || "Otro";
            const titulo = info.event.extendedProps.originalTitle || info.event.title;
            const descripcion = info.event.extendedProps.description || "Sin descripción";

            dialogTitle.textContent = tipo;
            dialogEvent.textContent = `Evento: ${titulo}`;
            dialogDescription.textContent = `Descripción: ${descripcion}`;
            dialogOverlay.style.display = "block";
            dialog.style.display = "flex";
        }
    });

    calendar.render();

    // Cerrar el cuadro de diálogo
    closeButton.addEventListener("click", function () {
        dialogOverlay.style.display = "none";
        dialog.style.display = "none";
    });

    // Obtener categorías únicas (Feriado Nacional + tipos de eventos académicos)
    const categoriasUnicas = ["Feriado Nacional", ...new Set(eventos.map(evento => evento.type))];

    // Rellenar el combobox con las categorías
    categoriasUnicas.forEach(categoria => {
        const option = document.createElement("option");
        option.value = categoria;
        option.textContent = categoria;
        filterSelect.appendChild(option);
    });

    // Manejar el cambio de filtro
    filterSelect.addEventListener("change", function () {
        const filter = this.value;

        // Filtrar eventos según la categoría seleccionada
        const filteredEvents = allEvents.filter(evento => {
            return filter === "all" || evento.type === filter;
        });

        // Actualizar el calendario con los eventos filtrados
        calendar.removeAllEvents();
        calendar.addEventSource(filteredEvents);
    });
});
