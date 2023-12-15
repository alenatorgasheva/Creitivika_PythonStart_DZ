x=1
q=0.01
r=255
g=226
b=0
def setup():
    background(0)
    size(1000,1000)
    

def draw():
    global x, q , r , g , b
    
    # planets
    push()
    fill(46,65,255)
    ellipse(950, 100, 100, 100)
    fill(149,48,52)
    ellipse(750, 550,30,30)
    fill(93,85,85)
    ellipse(850,50,50,50)
    fill(255,237,36)
    ellipse(350,50,200,200)
    fill(93,85,85)
    ellipse(850,50,50,50)
    fill(93,85,85)
    ellipse(850,50,50,50)
    pop()
    
    # meteorite
    push()
    x = x + 10
    noStroke()
    fill(r,g,b)
    ellipse(x, x, 80, 60)
    r=r-1
    g=g-1
    b=b-1
    pop()
    
    # stars
    push()
    stroke(random(0,255))
    strokeWeight(random(0,7))
    point(random(0,1000),random(0,1000))
    pop()
    
    #explosion
    push()
    if x >= 1000:
        translate(950,950)
            
        q = q + 0.1
        scale(q)
        noStroke()
        ellipse(0, 0, 80, 60)
    
    pop()
