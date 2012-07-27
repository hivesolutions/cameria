{% extends "partials/layout_full.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if sub_link == "show" %}
            <a href="{{ url_for('show_camera', id = camera.id) }}" class="active">show</a>
        {% else %}
            <a href="{{ url_for('show_camera', id = camera.id) }}">show</a>
        {% endif %}
        //
        {% if sub_link == "settings" %}
            <a href="{{ url_for('settings_camera', id = camera.id) }}" class="active">settings</a>
        {% else %}
            <a href="{{ url_for('settings_camera', id = camera.id) }}">settings</a>
        {% endif %}
        //
        {% if sub_link == "edit" %}
            <a href="#" class="active">edit</a>
        {% else %}
            <a href="#">edit</a>
        {% endif %}
    </div>
{% endblock %}
