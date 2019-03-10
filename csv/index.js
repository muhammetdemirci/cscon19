const brain = require("brain.js")

var net = new brain.NeuralNetwork()

// net.train([{ input: { numofbooks: 4325.0, internship: 6, homeworks: 5, participation: 10, community: 1 }, output: { AA: 1 } }, { input: { numofbooks: 423, internship: 33, homeworks: 55, participation: 820, community: 3 }, output: { AA: 1 } }, { input: { numofbooks: 7, internship: 2, homeworks: 2, participation: 8, community: 3 }, output: { DD: 1 } }, { input: { numofbooks: 5, internship: 1, homeworks: 2, participation: 4, community: 1 }, output: { DD: 1 } }, { input: { numofbooks: 8, internship: 1, homeworks: 2, participation: 12, community: 1 }, output: { DD: 1 } }])
net.train([{ input: { numofbooks: 4325, internship: 100, homeworks: 500, participation: 200, community: 2 }, output: { AA: 1, DD: 0 } }, { input: { numofbooks: 423, internship: 343, homeworks: 5500, participation: 820, community: 3 }, output: { AA: 1, DD: 0 } }, { input: { numofbooks: 7, internship: 2, homeworks: 2, participation: 8, community: 8 }, output: { AA: 0, DD: 1 } }, { input: { numofbooks: 5, internship: 1, homeworks: 2, participation: 4, community: 5 }, output: { AA: 0, DD: 1 } }, { input: { numofbooks: 8, internship: 1, homeworks: 2, participation: 12, community: 7 }, output: { AA: 0, DD: 1 } }])


var out = net.run({
  numofbooks: 1, internship: 1, homeworks: 2, participation: 20, community: 1
})

console.log('out ->', out)