const { exec } = require("child_process");

exec("python ../engine/beat_detector.py sample.mp3", (err, stdout, stderr) => {
    if (err) {
        console.error(`Error: ${stderr}`);
        return;
    }
    console.log(`Beat timestamps:\n${stdout}`);
});
