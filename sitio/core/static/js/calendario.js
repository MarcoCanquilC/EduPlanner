document.addEventListener("DOMContentLoaded", async function() {
    var calendarEl = document.getElementById("calendar");

    const calendarioData = await (await fetch("http://127.0.0.1:8000/api/calendario/")).json()
    
    var eventos = calendarioData.eventos.map(evento => ({
        title: evento.titulo,
        start: evento.fecha_inicio,
        end: evento.fecha_fin,
        description: evento.descripcion,
        color: evento.tipo === "examen" ? "red" : "blue"
    }))

    var feriados = calendarioData.feriados.map(feriado => ({
        title: feriado.nombre,
        start: feriado.fecha,
        color: "green",
        allDay: true
    }))

    var calendar = new FullCalendar.Calendar(calendarEl, {
        locale: "es",
        initialView: "dayGridMonth",
        events: [...eventos, ...feriados],
        eventClick: function(info) {
            alert(info.event.title + ": " + info.event.extendedProps.description);
        }
    })

    calendar.render()
});
