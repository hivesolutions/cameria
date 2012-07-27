{% extends "partials/layout.html.tpl" %}
{% block title %}Cameras{% endblock %}
{% block name %}Cameras{% endblock %}
{% block content %}
    <ul>
        {% for camera in cameras %}
            <li>
                <div class="name">
                    <a href="{{ url_for('show_camera', id = camera.id) }}">{{ camera.id }}</a>
                </div>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
