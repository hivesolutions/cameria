{% extends "partials/layout.html.tpl" %}
{% block title %}Devices{% endblock %}
{% block name %}Devices{% endblock %}
{% block content %}
    <ul>
        {% for device in devices %}
            <li>
                <div class="name capitalize">
                    <a href="{{ url_for('show_device', id = device.id) }}">{{ device.type }} {{ device.model }}</a>
                </div>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
