const pieCtx = document.getElementById("pieChart");
const barCtx = document.getElementById("barChart");

new Chart(pieCtx, {
  type: "doughnut",
  data: {
    labels: ["Occupied", "Vacant"],
    datasets: [
      {
        data: [75, 25],
        backgroundColor: ["#2563eb", "#e5e7eb"],
      },
    ],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
  },
});

new Chart(barCtx, {
  type: "bar",
  data: {
    labels: ["Jan", "Feb", "Mar", "Apr", "May"],
    datasets: [
      {
        label: "Income (KSh)",
        data: [350000, 420000, 390000, 450000, 480000],
        backgroundColor: "#2563eb",
      },
    ],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
  },
});
