{% extends "partials/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if "devices.show" in session.tokens %}
            {% if sub_link == "show" %}
                <a href="{{ url_for('show_device', id = device.id) }}" class="active">show</a>
            {% else %}
                <a href="{{ url_for('show_device', id = device.id) }}">show</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}
