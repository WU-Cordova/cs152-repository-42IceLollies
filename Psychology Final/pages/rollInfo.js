//adds "lobe" to the choices that need it
var choice = localStorage.getItem("choice");
if (
  choice == "occipital" ||
  choice == "parietal" ||
  choice == "frontal" ||
  choice == "temporal"
) {
  choice += " lobe";
}

//writes correct information in first p tags & rolls the die
window.onload = roll(parseInt(localStorage.getItem("numPoints")), choice);

//functions
//=======================================================================
function roll(numPoints, choice) {
  if (numPoints == 0) {
    document.getElementById("needToRoll").innerHTML =
      "Sorry, the " + choice + " won't help you in this situation.";
    document.getElementById("roll").style.display = "none";
    document.getElementById("passFail").style.display = "none";
  } else {
    document.getElementById("needToRoll").innerHTML =
      "You need to roll a " +
      Math.round(80 / numPoints) +
      " or above to use the " +
      choice +
      ".";
    //roll die
    var rollNum = Math.floor(Math.random() * 21);
    document.getElementById("roll").innerHTML = "Your roll: " + rollNum;
    document.getElementById("roll").style.display = "block";
    if (rollNum * numPoints >= 80) {
      document.getElementById("passFail").innerHTML = "Woohoo! You did it!";
    } else {
      document.getElementById("passFail").innerHTML =
        "You didn't roll high enough.";
    }
    document.getElementById("passFail").style.display = "block";

    //adds values to game totals
    if (numPoints == 13) {
      var current = parseInt(localStorage.getItem("correctAnswers"));
      localStorage.setItem("correctAnswers", current + 1);
    }
    var current = parseInt(localStorage.getItem("totalPoints"));
    localStorage.setItem("totalPoints", current + rollNum * numPoints);
  }
  console.log(localStorage.getItem("correctAnswers"));
  console.log(localStorage.getItem("totalPoints"));
}
