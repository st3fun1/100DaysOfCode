const fs = require('fs');
const os = require('os');

console.log(process);
fs.readFile('hello.py', 'utf-8', (err, data) => {
    if (err) {
        console.log(err);
    } else if (data) {
        console.log(data);
        let formatedData = '# added python comment\n' + data;
        // formatedData = formatedData.replace(/send_json\(\)/g, ' send_json()');
        // fs.writeFile('hello.py', formatedData, (err, data) => {
        //     console.log(err, data);
        // });
    }
});