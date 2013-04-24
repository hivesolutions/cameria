{% extends "partials/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if acl("sets.list") %}
            {% if sub_link == "list" %}
                <a href="{{ url_for('list_sets') }}" class="active">list</a>
            {% else %}
                <a href="{{ url_for('list_sets') }}">list</a>
            {% endif %}
        {% endif %}
        {% if acl("sets.new") %}
            //
            {% if sub_link == "create" %}
                <a href="{{ url_for('new_set') }}" class="active">create</a>
            {% else %}
                <a href="{{ url_for('new_set') }}">create</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}
