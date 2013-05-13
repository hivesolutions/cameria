{% extends "partials/layout_account.html.tpl" %}
{% block title %}Accounts{% endblock %}
{% block name %}Accounts :: {{ account.username }}{% endblock %}
{% block content %}
    <div class="quote">{{ account.username }}</div>
    <div class="separator-horizontal"></div>
    <table>
        <tbody>
            <tr>
                <td class="right label" width="50%">email</td>
                <td class="left value" width="50%">{{ account.email }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">type</td>
                <td class="left value" width="50%">{{ account.type_s() }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">cameras</td>
                <td class="left value" width="50%">
                    {% if account.cameras == None %}
                        <span>*</span>
                    {% elif account.cameras.objects == [] %}
                        <span>N/A</span>
                    {% else %}
                        {% for camera in account.cameras.objects %}
                            <a href="{{ url_for('show_camera', camera_id = camera.camera_id) }}">{{ camera.id }}</a>{% if not loop.last %},{% endif %}
                        {% endfor %}
                    {% endif %}
                </td>
            </tr>
        </tbody>
    </table>
{% endblock %}
