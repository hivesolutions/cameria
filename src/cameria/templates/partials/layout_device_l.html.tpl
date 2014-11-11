{% extends "partials/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if acl("devices.list") %}
            {% if sub_link == "list" %}
                <a href="{{ url_for('list_devices') }}" class="active">list</a>
            {% else %}
                <a href="{{ url_for('list_devices') }}">list</a>
            {% endif %}
        {% endif %}
        {% if acl("devices.new") %}
            //
            {% if sub_link == "create" %}
                <a href="{{ url_for('new_device') }}" class="active">create</a>
            {% else %}
                <a href="{{ url_for('new_device') }}">create</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}
