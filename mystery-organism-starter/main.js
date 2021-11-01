// Returns a random DNA base
const returnRandBase = () => {
  const dnaBases = ["A", "T", "C", "G"];
  return dnaBases[Math.floor(Math.random() * 4)];
};

// Returns a random single stand of DNA containing 15 bases
const mockUpStrand = () => {
  const newStrand = [];
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase());
  }
  return newStrand;
};

// Returns a Pila aequor object
const pAequorFactory = (specimenNum, dna) => {
  return {
    dna: dna,
    specimenNum: specimenNum,

    mutate() {
      const randI = Math.floor(Math.random() * 15);
      let randB = returnRandBase();
      while (this.dna[randI] === randB) {
        randB = returnRandBase();
      }
      this.dna[randI] = randB;
    },
    compareDNA(pAequor) {
      let match = 0;
      let index = 0;

      pAequor.dna.forEach((element) => {
        if (element === this.dna[index]) {
          match++;
        }
        index++;
      });

      let perMatch = Math.round((match * 100) / 15);

      console.log(
        `specimen #${this.specimenNum} and specimen #${pAequor.specimenNum} have ${perMatch}% DNA in common`
      );
    },
    willLikelySurvive() {
      let match = 0;

      this.dna.forEach((element) => {
        if (element === "C" || element === "G") {
          match++;
        }
      });

      let perMatch = Math.round((match * 100) / 15);

      return perMatch > 60 ? true : false;
    },
  };
};

//testing factory
const pA1 = pAequorFactory(1, mockUpStrand());
console.log(pA1.dna);
//testing mutate
pA1.mutate();
console.log(pA1.dna);
//testing compare
pA1.compareDNA(pA1);
const pA2 = pAequorFactory(2, mockUpStrand());
pA2.compareDNA(pA1);
//testing survival
console.log(pA1.willLikelySurvive());
console.log(pA2.willLikelySurvive());
//populating
const dnaArray = [];
dnaArray.push(pA1);
dnaArray.push(pA2);

for (let i = 2; i < 30; i++) {
  dnaArray.push(pAequorFactory(i, mockUpStrand()));
}
