{% extends "partials/layout_full.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if acl("sets.show") %}
            {% if sub_link == "show" %}
                <a href="{{ url_for('show_set', set_id = set.set_id) }}" class="active">show</a>
            {% else %}
                <a href="{{ url_for('show_set', set_id = set.set_id) }}">show</a>
            {% endif %}
        {% endif %}
        {% if acl("sets.edit") %}
            //
            {% if sub_link == "edit" %}
                <a href="{{ url_for('edit_set', set_id = set.set_id) }}" class="active">edit</a>
            {% else %}
                <a href="{{ url_for('edit_set', set_id = set.set_id) }}">edit</a>
            {% endif %}
        {% endif %}
        {% if acl("sets.settings") %}
            //
            {% if sub_link == "settings" %}
                <a href="{{ url_for('settings_set', set_id = set.set_id) }}" class="active">settings</a>
            {% else %}
                <a href="{{ url_for('settings_set', set_id = set.set_id) }}">settings</a>
            {% endif %}
        {% endif %}
        {% if acl("sets.delete") %}
            //
            {% if sub_link == "delete" %}
                <a href="{{ url_for('delete_set', set_id = set.set_id) }}" class="active warning link-confirm"
                   data-message="Do you really want to delete {{ set.set_id }}  ?">delete</a>
            {% else %}
                <a href="{{ url_for('delete_set', set_id = set.set_id) }}" class="warning link-confirm"
                   data-message="Do you really want to delete {{ set.set_id }} ?">delete</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}
