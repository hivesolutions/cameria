{% extends "partials/layout.html.tpl" %}
{% block title %}Users{% endblock %}
{% block name %}Users :: {{ user.username }}{% endblock %}
{% block content %}
    <div class="quote capitalize">{{ user.name }}</div>
    <div class="separator-horizontal"></div>
    <table>
        <tbody>
            <tr>
                <td class="right label" width="50%">tokens</td>
                <td class="left value" width="50%">
                    {% for token in user.tokens %}
                        {{ token }}{% if not loop.last %},{% endif %}
                    {% endfor %}
                </td>
            </tr>
            <tr>
                <td class="right label" width="50%">cameras</td>
                <td class="left value" width="50%">
                    {% if not "user" in cameras or user.cameras == None %}
                        all
                    {% else %}
                        {% for camera in user.cameras %}
                            <a href="{{ url_for('show_camera', id = camera) }}">{{ camera }}</a>{% if not loop.last %},{% endif %}
                        {% endfor %}
                    {% endif %}
                </td>
            </tr>
        </tbody>
    </table>
{% endblock %}
