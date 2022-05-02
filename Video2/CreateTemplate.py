# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:29:35 2022

@author: Damian @cardanotrees
"""

########################################
# Define the parameters
AssetName = 'test2'
NLayers = 1
########################################

####################################################
# Do not modify from here
####################################################
fout = open(AssetName+'.html', 'w')

text = "<html><style>*{margin:0; padding:0;}html, body {width:100%; height:100%;}myCanvas { display:block;}</style><body style='background-color:black;'><section><div id='canvasesdiv' style='position:relative; width:100%; height:100%'>"
print(text, file=fout)

for ii in range(NLayers):
    text="<canvas id='layer"+str(ii+1)+"' style='z-index: "+str(ii+1)+";position:absolute;left:0px;top:0px;'></canvas>"
    print(text, file=fout)

print('</div>', file=fout)
print('<script>', file=fout)

for ii in range(NLayers):
    text="    function "+AssetName+"I"+str(ii+1)+"(){"
    print(text, file=fout)
    print("    }", file=fout)
    text="    function "+AssetName+"D"+str(ii+1)+"(){"
    print(text, file=fout)
    text="        //ssx=window.innerWidth;ssy=window.innerHeight;ss=Math.min(ssx,ssy);"
    print(text, file=fout)
    text="        //"+AssetName+"ctx"+str(ii+1)+".clearRect(0, 0, ssx, ssy);"
    print(text, file=fout)
    text="        //setTimeout(function(){window.requestAnimationFrame(function(){"+AssetName+"D"+str(ii+1)+"()})},16)"
    print(text, file=fout)  
    print("    }", file=fout)

print("</script>", file=fout)
print("<script>", file=fout)

for ii in range(NLayers):
    text="    const canvas"+str(ii+1)+" = document.getElementById('layer"+str(ii+1)+"'); const "+AssetName+"ctx"+str(ii+1)+" = canvas"+str(ii+1)+".getContext('2d');"
    print(text, file=fout)

text="    var WIDTH = window.innerWidth; var HEIGHT = window.innerHeight;"
print(text, file=fout)

for ii in range(NLayers):
    text="    canvas"+str(ii+1)+".width = WIDTH; canvas"+str(ii+1)+".height = HEIGHT;"
    print(text, file=fout)

text="    function resizeCanvas() {"
print(text, file=fout)
text="        WIDTH = window.innerWidth; HEIGHT = window.innerHeight;"
print(text, file=fout)

for ii in range(NLayers):
    text="        canvas"+str(ii+1)+".width = WIDTH; canvas"+str(ii+1)+".height = HEIGHT;"
    print(text, file=fout)
    
text="        location.reload();"
print(text, file=fout)
text="    }"
print(text, file=fout)

text="    window.addEventListener('resize', resizeCanvas, false);"
print(text, file=fout)

text="    function InitAll(){"
print(text, file=fout)
for ii in range(NLayers):
    text="        "+AssetName+"I"+str(ii+1)+"();"
    print(text, file=fout)
text="        DrawAll();"
print(text, file=fout)  
print("    }", file=fout)

text="    function DrawAll(){"
print(text, file=fout)
for ii in range(NLayers):
    text="        "+AssetName+"D"+str(ii+1)+"();"
    print(text, file=fout)
print("    }", file=fout)

text="    InitAll();"
print(text, file=fout)

print("</script>", file=fout)
print("</section>", file=fout)
print("</body>", file=fout)
print("</html>", file=fout)
    
fout.close()