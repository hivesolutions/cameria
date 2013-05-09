{% extends "partials/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if acl("devices.show") %}
            {% if sub_link == "show" %}
                <a href="{{ url_for('show_device', device_id = device.device_id) }}" class="active">show</a>
            {% else %}
                <a href="{{ url_for('show_device', device_id = device.device_id) }}">show</a>
            {% endif %}
        {% endif %}
        {% if acl("devices.edit") %}
            //
            {% if sub_link == "edit" %}
                <a href="{{ url_for('edit_device', device_id = device.device_id) }}" class="active">edit</a>
            {% else %}
                <a href="{{ url_for('edit_device', device_id = device.device_id) }}">edit</a>
            {% endif %}
        {% endif %}
        {% if acl("devices.delete") %}
            //
            {% if sub_link == "delete" %}
                <a href="{{ url_for('delete_device', device_id = device.device_id) }}" class="active warning link-confirm"
                   data-message="Do you really want to delete {{ device.device_id }}  ?">delete</a>
            {% else %}
                <a href="{{ url_for('delete_device', device_id = device.device_id) }}" class="warning link-confirm"
                   data-message="Do you really want to delete {{ device.device_id }} ?">delete</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}
