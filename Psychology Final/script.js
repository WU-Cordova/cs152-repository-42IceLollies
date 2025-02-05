/*
numbers of sections:
1- amygdala - s1
2- brainstem - s2
3- cerabellum - s3
4- frontal lobe - s4
5- hippocampus - s5
6- hypothalamus - s6
7- occipital lobe - s7
8- parietal lobe - s8
9- temporal lobe - s9
10-thalamus - s10
*/

//variables
//===========================================================================

var level = parseInt(localStorage.getItem("level"), 10);
var choice = localStorage.getItem("choice");
//each object represents one level, each property is the points for one selection in that level's situation
var points = [
  [4, 5, 8, 7, 0, 13, 0, 0, 0, 0],
  [0, 0, 6, 7, 0, 0, 12, 0, 13, 10],
  [10, 0, 0, 10, 13, 0, 12, 0, 9, 6],
  [13, 0, 0, 12, 6, 9, 0, 0, 0, 0],
  [],
];

/*
 the rest of the levels - I'll fill them in later after i work out soem more of the point
 {s1:, s2:, s3:, s4:, s5:, s6:, s7:, s8:, s9:, s10:,},
  */

//OnClick functions
//===========================================================================

//switches page and levels up/ selects a choice to save in local storage if required by button
function switchPage(newPage, levelUp, lockChoice) {
  window.location.href = newPage;

  if (levelUp == true) {
    localStorage.setItem("level", level + 1);
  }
  if (lockChoice == true) {
    if (choice == "null") {
      alert("Please choose an option");
      window.location.href = "select.html";
    }
    localStorage.setItem("choice", choice);
    setPoints();
  }
}

//sets choice equal to selected brain part
function setChoice(section) {
  var borderOff = document.getElementsByTagName("img");
  for (var i = 0; i < borderOff.length; i++) {
    borderOff[i].style.borderColor = "black";
  }
  document.getElementById(section).style.borderColor = "purple";
  choice = section;
}

//Game Funtionality
//===========================================================================

function setPoints() {
  var idx;
  switch (choice) {
    case "amygdala":
      idx = 0;
      break;
    case "brainstem":
      idx = 1;
      break;
    case "cerebellum":
      idx = 2;
      break;
    case "frontal":
      idx = 3;
      break;
    case "hippocampus":
      idx = 4;
      break;
    case "hypothalamus":
      idx = 5;
      break;
    case "occipital":
      idx = 6;
      break;
    case "parietal":
      idx = 7;
      break;
    case "temporal":
      idx = 8;
      break;
    case "thalamus":
      idx = 9;
      break;
  }
  localStorage.setItem("numPoints", points[level][idx]);
}
