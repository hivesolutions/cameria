{% extends "partials/layout_simple.html.tpl" %}
{% block title %}Users{% endblock %}
{% block name %}Users :: {{ user.username }}{% endblock %}
{% block content %}
    <div class="quote capitalize">{{ user.name }}</div>
    <div class="separator-horizontal"></div>
    <table>
        <tbody>
            <tr>
                <td class="right label" width="50%">password</td>
                <td class="left value" width="50%">{{ user.password }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">tokens</td>
                <td class="left value" width="50%">{{ user.tokens }}</td>
            </tr>
            <tr>
                <td class="right label" width="50%">cameras</td>
                <td class="left value" width="50%">{{ user.cameras }}</td>
            </tr>
        </tbody>
    </table>
{% endblock %}
