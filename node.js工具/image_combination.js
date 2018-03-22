var json = require("./demo.json");
var a = `<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>frames</key>
        <dict>
        `;
 
 for(var i in json.frames){
     var temp = json.frames[i];
     var r = `<key>${i}.png</key>
            <dict>
                <key>frame</key>
                <string>{{${temp.x},${temp.y}},{${temp.w},${temp.h}}}</string>
                <key>offset</key>
                <string>{0,0}</string>
                <key>rotated</key>
                <false/>
                <key>sourceColorRect</key>
                <string>{{0,0},{${temp.sourceW},${temp.sourceH}}</string>
                <key>sourceSize</key>
                <string>{${temp.sourceW},${temp.sourceH}}</string>
            </dict>
            `;
     a += r;
 }
 
 a += `
        </dict>
        <key>metadata</key>
        <dict>
            <key>format</key>
            <integer>2</integer>
            <key>realTextureFileName</key>
            <string>itemicon1.png</string>
            <key>size</key>
            <string>{1024,2048}</string>
            <key>smartupdate</key>
            <string>$TexturePacker:SmartUpdate:72c74d80f7ebe244088386e531441fd1:1/1$</string>
            <key>textureFileName</key>
            <string>itemicon1.png</string>
        </dict>
    </dict>
</plist>
`;

var fs =require("fs");
fs.writeFile("demo.plist", a);