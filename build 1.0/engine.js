document.addEventListener("DOMContentLoaded", async () => {
    const response = await fetch("players.csv");
    const data = await response.text();
    const rows = data.split("\n").map(row => row.split(","));
    
    let teams = new Set();
    let years = new Set();
    
    rows.forEach(row => {
        years.add(row[0]); // Assuming column 0 is the year
        teams.add(row[1]); // Assuming column 1 is the team name
    });

    const yearSelect = document.getElementById("year");
    const teamSelect = document.getElementById("team");

    years.forEach(year => {
        yearSelect.innerHTML += `<option value="${year}">${year}</option>`;
    });

    teams.forEach(team => {
        teamSelect.innerHTML += `<option value="${team}">${team}</option>`;
    });
});

function updatePlayers() {
    const selectedYear = document.getElementById("year").value;
    const selectedTeam = document.getElementById("team").value;
    fetch(`get_players.py?year=${selectedYear}&team=${selectedTeam}`)
        .then(response => response.json())
        .then(players => {
            const playerList = document.getElementById("playerList");
            playerList.innerHTML = "";
            players.forEach(player => {
                playerList.innerHTML += `<li>${player}</li>`;
            });
        });
}
