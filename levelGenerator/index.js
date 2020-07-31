const XMLHttpRequest = require('xmlhttprequest').XMLHttpRequest;
const fs = require('fs')

var url = "http://colormind.io/api/";
var data = {
	model : "default",
}

var http = new XMLHttpRequest();

var palettes = []

http.onreadystatechange = function() {
	if(http.readyState == 4 && http.status == 200) {
    var palette = JSON.parse(http.responseText).result;
    palettes.push(palette)
	}
}
for(var i = 0;i < 37;i++){
  http.open("POST", url, false);
  http.send(JSON.stringify(data));
}


for(var i = 0; i < 37;i++){
  palettes[i].pop()
}

levels = []

for(var i = 0; i < 36;i++){
  lev = {
    "color": palettes[i],
    "dimensions": randomDim(),
    "scrambled": randomScramble(),
    "solved": false
  }
  levels.push(lev)
}

area = {
  "color": palettes.pop(),
  "levels": levels
}

function randomDim(){
  x = getRandomInt(2,5)*2+1
  return [x,x]
}

function randomScramble(){
  scrambles = ["checkerboard","barsInner","corners","frame","barsOuter","lane"]
  return scrambles[getRandomInt(0,scrambles.length -1)]
}

function getRandomInt(min,max){
  return Math.floor(Math.random()*Math.floor(max-min)+Math.floor(min))
}

console.log(area.levels[0].color)

var areaJSON = JSON.stringify(area)

fs.writeFile('area.json',areaJSON,(err)=>{
  if(err){
    throw err;
  }
  console.log("data is saved")
})