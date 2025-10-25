let Month = 12;
let fortunes = [
  "Vous passerez une excellente journée !",
  "De bonnes choses arrivent !",
  "Faites attention, quelque chose d'inattendu pourrait se produire !",
  "Vous rencontrerez quelqu'un de nouveau aujourd'hui !",
  "Vous aurez une fête surprise ce soir !",
  "Vous obtiendrez une promotion au travail !",
  "Vous trouverez un billet de 20 $ dans la rue !",
  "Vous passerez un merveilleux week-end !",
];

if (Month === 1) {
  console.log("Capricorn", fortunes[0]);
} else if (Month === 2) {
  console.log("Aquarius", fortunes[1]);
} else if (Month === 3) {
  console.log("Pisces", fortunes[2]);
} else if (Month === 4) {
  console.log("Aries", fortunes[3]);
} else if (Month === 5) {
  console.log("Taurus", fortunes[4]);
} else if (Month === 6) {
  console.log("Gemini", fortunes[5]);
} else if (Month === 7) {
  console.log("Cancer", fortunes[6]);
} else if (Month === 8) {
  console.log("Leo", fortunes[7]);
} else if (Month === 9) {
  console.log("Virgo", fortunes[3]);
} else if (Month === 10) {
  console.log("Libra", fortunes[2]);
} else if (Month === 11) {
  console.log("Scorpio", fortunes[5]);
} else if (Month === 12) {
  console.log("Sagittarius", fortunes[6]);
} else {
  console.log("Invalid Month");
}
