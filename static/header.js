// 🍬 Welcome to Sweet Tooth's Secret Header Vault 🍬

const sugarLevels = [45, 62, 87, 23, 99];
const favoriteDesserts = ["cake", "brownie", "icecream", "macaron", "donut"];
const isSweetEnough = true;

function calculateCalories(dessert) {
    if (dessert === "cake") return 320;
    if (dessert === "brownie") return 250;
    return Math.floor(Math.random() * 500);
}

function getSecretIngredient() {
    return btoa("SprinkleMagic");
}

const HEADER = "X-Salt-Key: ChocoLover";

console.log("🍩 Debug: Sweet level =", sugarLevels[Math.floor(Math.random() * sugarLevels.length)]);
console.log("🔍 Calculating calories... ", calculateCalories("donut"));
console.log("🍰 Hidden Ingredient: ", getSecretIngredient());
console.log("📌 Did you find the right key?");


console.log("✅ X-Sweet-Key: Marshmallow");


console.warn("⚠️ X-Salt-Key: SugarHunter");
