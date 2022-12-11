import { input } from "./Day-10.input.js";

console.log("input : ", typeof input);
const data = input.split("\n");

const firstSignalCycleRange = 20;
const otherSignalCycleRange = 40;
const numberOfCycleX = 2;
const numberOfCycleNoop = 1;

let currentCycle = 1;
let theX = 1;

const signalStrenghts = [];

const getXValue = (command) => {
  if (command.includes("addx")) {
    const commandData = command.split(" ");
    return Number(commandData[1]);
  }

  return 0;
};

const getCycleCount = (command) => {
  if (command.includes("addx")) {
    return numberOfCycleX;
  }

  return numberOfCycleNoop;
};

data.map((command, commandIndex) => {
  console.log("\n");
  currentCycle += getCycleCount(command);
  console.log("currentCycle = ", currentCycle);

  theX += getXValue(command);
  console.log("the x = ", theX);

  const nextSignalCycleRange =
    otherSignalCycleRange * signalStrenghts.length + firstSignalCycleRange;

  if (currentCycle === nextSignalCycleRange) {
    signalStrenghts.push(theX * nextSignalCycleRange);
  } else {
    /* Check if next cycle is passing the current nextSignalCycleRange */
    /* If yes, it means we need to make the current cycle as the signal strength */
    try {
      const nextCommand = data[commandIndex + 1];
      const nextCycle = getCycleCount(nextCommand) + currentCycle;

      if (
        currentCycle < nextSignalCycleRange &&
        nextCycle > nextSignalCycleRange
      ) {
        signalStrenghts.push(theX * nextSignalCycleRange);
      }
    } catch {
      /* Last loop will throw error */
      /* Do nothing */
    }
  }
});

console.log("\n==========================\n");
console.log("signalStrenghts : ", signalStrenghts);
console.log("\n==========================\n");
console.log(
  "total : ",
  signalStrenghts.reduce((a, b) => a + b, 0)
);
console.log("\n==========================\n");

const cycleRange = 40;
const crtRows = [];
let crtRow = [];
currentCycle = 1;

const spriteSize = 3;

let currentPosition = 0;
let oldPosition = 0;

/* Part 2 */
data.map((command, commandIndex) => {
  console.log("\n\n");
  console.log("command = ", command);
  console.log("currentCycle = ", currentCycle);

  currentPosition += getXValue(command);
  console.log("debug oldPosition : ", oldPosition);
  console.log("debug currentPosition : ", currentPosition);

  const cycleCount = getCycleCount(command);
  currentCycle += cycleCount;

  /* Get the # or . */
  for (let i = 0; i < getCycleCount(command); i++) {
    const activeNewRowPosition = crtRow.length;
    console.log("activeNewRowPosition : ", activeNewRowPosition);

    const leftRange = oldPosition;
    const rightRange = leftRange + spriteSize - 1;
    console.log("leftRange : ", leftRange);
    console.log("rightRange : ", rightRange);
    if (
      activeNewRowPosition >= leftRange &&
      activeNewRowPosition <= rightRange
    ) {
      crtRow.push("#");
    } else {
      crtRow.push(".");
    }

    console.log("crtRow.length : ", crtRow.length);

    if (cycleRange === crtRow.length) {
      crtRows.push(crtRow);
      crtRow = [];
    }
  }
  console.log("crtRow : ", crtRow.join(""));

  oldPosition = currentPosition;
});

console.log("\n==========================\n");
console.log(
  "crtRows : ",
  crtRows.map((row) => row.join(""))
);
console.log("\n==========================\n");
