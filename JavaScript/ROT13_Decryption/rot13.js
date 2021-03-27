const lower = "abcdefghijklmnopqrstuvwxyz";
const upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const rotateChar = (char) => {
    if (lower.includes(char)) {
        const newIdx = (lower.indexOf(char) + 13) % lower.length;
        return lower[newIdx];
    }
    if (upper.includes(char)) {
        const newIdx = (upper.indexOf(char) + 13) % upper.length;
        return upper[newIdx];
    }
    return char;
}

const rotate13 = (string) => {
    const stringArray = string.split("");
    const rotatedBy13 = stringArray.map((char) => rotateChar(char));
    return rotatedBy13.join("");
}

const exit = () => {
    console.log('Usage: please provide a string to encrypt');
    process.exit();
}

const main = (input) => {
    try {
        input.length > 0 ? console.log(rotate13(input)): exit();
    } catch {
        exit();
    }
}

main(process.argv[2]);
main(process.argv[2]);
