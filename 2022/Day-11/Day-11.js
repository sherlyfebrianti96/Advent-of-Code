import { input } from "./Day-11.input.js";

console.log("input : ", input);
const data = input.split("\n");

let monkeys = new Set();
let activeMonkey = 0;
let items = [];
let operations = [];
let divisible = [];
let divisibleTrue = [];
let divisibleFalse = [];

data.map((command) => {
  /* Active Monkey */
  const activeMonkeyPattern = /Monkey \d:/g;

  /* Items */
  const itemsPattern = "Starting items: ";

  /* Operation */
  const operationsPattern = "Operation: new = ";

  /* Divisible */
  const divisiblePattern = "Test: divisible";

  /* DivisibleTruePattern */
  const divisibleTruePattern = "If true: throw to";

  /* DivisibleFalsePattern */
  const divisibleFalsePattern = "If false: throw to";

  if (command.match(activeMonkeyPattern)) {
    /* Active Monkey */
    activeMonkey = Number(command.replace(/\D/g, ""));
    monkeys.add(activeMonkey);
  } else if (command.includes(itemsPattern)) {
    /* Items */
    const itemsData = command.replace(itemsPattern, "");
    items[activeMonkey] = itemsData.split(", ");
  } else if (command.includes(operationsPattern)) {
    /* Operations */
    const operationsData = command.replace(operationsPattern, "");
    operations[activeMonkey] = operationsData.replaceAll(" ", "");
  } else if (command.includes(divisiblePattern)) {
    /* Divisible */
    const divisibleData = Number(command.replace(/\D/g, ""));
    divisible[activeMonkey] = divisibleData;
  } else if (command.includes(divisibleTruePattern)) {
    /* Divisible true */
    const divisibleTrueData = Number(command.replace(/\D/g, ""));
    divisibleTrue[activeMonkey] = divisibleTrueData;
  } else if (command.includes(divisibleFalsePattern)) {
    /* Divisible false */
    const divisibleFalseData = Number(command.replace(/\D/g, ""));
    divisibleFalse[activeMonkey] = divisibleFalseData;
  }
});

console.log("Monkeys :", monkeys);
console.log("activeMonkey :", activeMonkey);
console.log("items :", items);
console.log("operations :", operations);
console.log("divisible :", divisible);
console.log("divisibleTrue :", divisibleTrue);
console.log("divisibleFalse :", divisibleFalse);

const numberOfRound = 20;
const inspectedItems = Array(monkeys.size).fill(0);

for (let round = 0; round < numberOfRound; round++) {
  console.log("\n--------------------\n");
  console.log("Round ", round);
  console.log("\n---------\n");

  Array.from(monkeys).map((monkey) => {
    console.log("Monkey :", monkey);

    items[monkey].map((item) => {
      console.log("~~~~~~~~~~");
      console.log("item :", item);
      console.log("operation :", operations[monkey]);

      inspectedItems[monkey] += 1;

      const operation = operations[monkey].replaceAll("old", item);
      const worryLevel = eval(operation);
      console.log("worryLevel : ", worryLevel);

      const worryLevelAfterBored = Math.floor(worryLevel / 3);
      console.log("worryLevelAfterBored : ", worryLevelAfterBored);

      /* Parse to next monkey */
      const divisionComparator = divisible[monkey];
      if (worryLevelAfterBored % divisionComparator === 0) {
        /* Monkey for divisibleTrue */
        const nextMonkey = divisibleTrue[monkey];
        console.log("debug nextMonkey : ", nextMonkey);
        items[nextMonkey] = [...items[nextMonkey], worryLevelAfterBored];
      } else {
        /* Monkey for divisibleFalse */
        const nextMonkey = divisibleFalse[monkey];
        console.log("debug nextMonkey : ", nextMonkey);
        items[nextMonkey] = [...items[nextMonkey], worryLevelAfterBored];
      }
      console.log("Current item : ", item);
    });
    /* Empty the monkey's stash */
    items[monkey] = [];

    console.log("\n");
  });

  console.log("Items : ", items);
}
console.log("\n==========================\n");
console.log("inspectedItems : ", inspectedItems);
console.log("\n==========================\n");
const sortedInspectedItems = inspectedItems.sort((a, b) => b - a);
console.log("sortedInspectedItems : ", sortedInspectedItems);
console.log("\n==========================\n");
console.log(
  "2 most active monkey's businesses : ",
  sortedInspectedItems[0] * sortedInspectedItems[1]
);
console.log("\n==========================\n");
