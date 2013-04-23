{% extends "partials/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if acl("cameras.show") %}
            {% if sub_link == "show" %}
                <a href="{{ url_for('show_camera', camera_id = camera.camera_id) }}" class="active">show</a>
            {% else %}
                <a href="{{ url_for('show_camera', camera_id = camera.camera_id) }}">show</a>
            {% endif %}
        {% endif %}
        {% if acl("cameras.edit") %}
            //
            {% if sub_link == "edit" %}
                <a href="{{ url_for('edit_camera', camera_id = camera.camera_id) }}" class="active">edit</a>
            {% else %}
                <a href="{{ url_for('edit_camera', camera_id = camera.camera_id) }}">edit</a>
            {% endif %}
        {% endif %}
        {% if acl("cameras.settings") %}
            //
            {% if sub_link == "settings" %}
                <a href="{{ url_for('settings_camera', camera_id = camera.camera_id) }}" class="active">settings</a>
            {% else %}
                <a href="{{ url_for('settings_camera', camera_id = camera.camera_id) }}">settings</a>
            {% endif %}
        {% endif %}
        {% if acl("cameras.delete") %}
            //
            {% if sub_link == "delete" %}
                <a href="{{ url_for('delete_camera', camera_id = camera.camera_id) }}" class="active warning link-confirm"
                   data-message="Do you really want to delete {{ camera.camera_id }}  ?">delete</a>
            {% else %}
                <a href="{{ url_for('delete_camera', camera_id = camera.camera_id) }}" class="warning link-confirm"
                   data-message="Do you really want to delete {{ camera.camera_id }} ?">delete</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}
