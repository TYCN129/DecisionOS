"use strict";

const STATE_FILE = "state.json";

document.addEventListener("DOMContentLoaded", initialize);

async function initialize() {
    try {
        const state = await loadState();

        renderSystem(state);
        renderCampaign(state);
        renderToday(state);
        renderExecution(state);
        renderHealth(state);
        renderAttention(state);
        renderAutopilot(state);
        renderRecovery(state);
        renderFooter(state);

    } catch (error) {

        console.error(error);

        document.body.innerHTML = `
            <div style="padding:40px;font-family:sans-serif;">
                <h1>DecisionOS</h1>
                <p>Unable to load state.json</p>
                <pre>${error}</pre>
            </div>
        `;
    }
}

async function loadState() {

    const response = await fetch(STATE_FILE);

    if (!response.ok) {
        throw new Error("Unable to read docs/state.json");
    }

    return await response.json();
}

function renderSystem(state) {

    setText("system-version", `Version ${state.system.version}`);

    setText("system-mode", state.system.mode);
}

function renderCampaign(state) {

    setText("campaign-name", state.campaign.name);

    setText("campaign-week", state.campaign.week);

    setText("campaign-status", state.campaign.status);

    populateList(
        "campaign-primary-list",
        state.campaign.primary
    );

    populateList(
        "campaign-secondary-list",
        state.campaign.secondary
    );

    populateList(
        "campaign-maintenance-list",
        state.campaign.maintenance
    );

    populateList(
        "campaign-success-criteria-list",
        state.campaign.success_criteria
    );
}

function renderToday(state) {

    setText("mission", state.today.mission);

    setText(
        "success-definition",
        state.today.success_definition
    );

    populateList(
        "maintenance-list",
        state.today.maintenance
    );

    populateList(
        "risk-list",
        state.today.known_risks
    );
}

function renderExecution(state) {

    setBoolean(
        "mission-status",
        state.execution.mission_completed
    );

    setBoolean(
        "artifact-status",
        state.execution.artifact_created
    );
}

function renderHealth(state) {

    setText(
        "sleep-hours",
        `${state.health.sleep_hours} hrs`
    );

    setBoolean(
        "gym-status",
        state.health.gym_completed
    );

    setText(
        "nutrition-status",
        state.health.nutrition
    );

    setText(
        "energy-status",
        state.health.energy
    );
}

function renderAttention(state) {
    const table = document.getElementById("attention-table");

    table.innerHTML = "";

    const attention = state.compass.attention;

    Object.entries(attention).forEach(([area, value]) => {

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${capitalize(area)}</td>
            <td>${value}%</td>
        `;

        table.appendChild(row);

    });
}

function renderAutopilot(state) {

    setText(
        "observation",
        state.autopilot.last_observation || "-"
    );

    setText(
        "root-cause",
        state.autopilot.root_cause || "-"
    );

    setText(
        "recommendation",
        state.autopilot.recommendation || "-"
    );
}

function renderRecovery(state) {

    setBoolean(
        "recovery-active",
        state.recovery.active
    );

    setText(
        "recovery-level",
        state.recovery.level
    );
}

function renderFooter(state) {

    setText(
        "dashboard-footer",
        state.dashboard.footer
    );

    setText(
        "last-updated",
        `Last Updated: ${state.system.last_updated ?? "-"}`
    );
}

function populateList(id, items) {

    const list = document.getElementById(id);

    list.innerHTML = "";

    if (!items || items.length === 0) {

        const li = document.createElement("li");

        li.textContent = "-";

        list.appendChild(li);

        return;
    }

    items.forEach(item => {

        const li = document.createElement("li");

        li.textContent = item;

        list.appendChild(li);

    });
}

function setText(id, value) {

    const element = document.getElementById(id);

    if (!element) return;

    element.textContent = value ?? "-";
}

function setBoolean(id, value) {

    const element = document.getElementById(id);

    if (!element) return;

    element.textContent = value ? "Yes" : "No";

    element.classList.remove(
        "status-success",
        "status-danger"
    );

    element.classList.add(
        value ? "status-success" : "status-danger"
    );
}

function capitalize(text) {

    if (!text) return "";

    return text
        .replace(/_/g, " ")
        .replace(/\b\w/g, c => c.toUpperCase());
}