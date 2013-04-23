{% extends "partials/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if acl("cameras.list") %}
            {% if sub_link == "list" %}
                <a href="{{ url_for('list_cameras') }}" class="active">list</a>
            {% else %}
                <a href="{{ url_for('list_cameras') }}">list</a>
            {% endif %}
        {% endif %}
        {% if acl("cameras.new") %}
            //
            {% if sub_link == "create" %}
                <a href="{{ url_for('new_camera') }}" class="active">create</a>
            {% else %}
                <a href="{{ url_for('new_camera') }}">create</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}
