{% extends "partials/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if sub_link == "show" %}
            <a href="{{ url_for('show_device', id = device.id) }}" class="active">show</a>
        {% else %}
            <a href="{{ url_for('show_device', id = device.id) }}">show</a>
        {% endif %}
        //
        {% if sub_link == "edit" %}
            <a href="#" class="active">edit</a>
        {% else %}
            <a href="#">edit</a>
        {% endif %}
    </div>
{% endblock %}
