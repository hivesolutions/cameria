{% extends "partials/layout_full.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if "sets.show" in session.tokens %}
            {% if sub_link == "show" %}
                <a href="{{ url_for('show_set', id = set.id) }}" class="active">show</a>
            {% else %}
                <a href="{{ url_for('show_set', id = set.id) }}">show</a>
            {% endif %}
        {% endif %}
        {% if "sets.settings" in session.tokens %}
            //
            {% if sub_link == "settings" %}
                <a href="{{ url_for('settings_set', id = set.id) }}" class="active">settings</a>
            {% else %}
                <a href="{{ url_for('settings_set', id = set.id) }}">settings</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}
