def collage():
  setMediaPath()
  original = makePicture(getMediaPath("track.jpg"))
  mod1 = makePicture(getMediaPath("track.jpg"))
  mod2 = makePicture(getMediaPath("track.jpg"))
  mod3 = makePicture(getMediaPath("track.jpg"))
  mod4 = makePicture(getMediaPath("track.jpg"))
  canvas = makeEmptyPicture(getWidth(original) * 2, getHeight(original) * 2)
  target = makePicture(getMediaPath("image.jpg"))
  
  
  
  
  
    
  
 
  edge(mod1)
  negative(mod2)
  negative(mod3)
  darken(mod4)
  
  
  
  copy(mod1, canvas, 0, 0)
  copy(mod2, canvas, getWidth(mod2), 0)
  copy(mod3, canvas, 0, getHeight(mod3))
  copy(mod4, canvas, getWidth(mod4), getHeight(mod4))
  copy(original, canvas, getWidth(canvas) / 4 , getHeight(canvas) / 2 )
  blend(target,canvas)
  
  show(canvas)
  
def copy(pic,target,targX,targY):
  targetX = targX
  for x in range(getWidth(pic)):
    targetY = targY
    for y in range(getHeight(pic)):
      pixel = getPixel(pic,x,y)
      tx = getPixel(target,targetX,targetY)
      setColor(tx,getColor(pixel))
      targetY=targetY+1
    targetX = targetX+1

def darken(pic):
  for each_pixel in getPixels(pic):
    color = getColor(each_pixel)
    color = makeDarker(color)
    setColor(each_pixel, color)
      
def negative(pic):
  for each_pixel in getPixels(pic):
    r = getRed(each_pixel)
    b = getBlue(each_pixel)
    g = getGreen(each_pixel) 
    neg = makeColor(255-r, 255-g, 255-b)
    setColor(each_pixel, neg)
      
def edge(picture):
  for px in getPixels(picture):
    x = getX(px)
    y = getY(px)
    if y < getHeight(picture) - 1 and x < getWidth(picture) - 1:
      sum = getRed(px)+getGreen(px)+getBlue(px)
      botrt = getPixel(picture, x+1, y+1)
      sum2 = getRed(botrt)+getGreen(botrt)+getBlue(botrt)
      diff = abs(sum2-sum)
      newcolor = makeColor(diff, diff, diff)
      setColor(px,newcolor)
 
 
def blend(source, target):
 for start in range(2):
   for x in range(start, getWidth(source), 2):
     for y in range(start, getHeight(source), 2):
       sourcePx = getPixel(source, x, y)
       targetPx = getPixel(target, x, y)
       setColor(targetPx, getColor(sourcePx))

collage()



