#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
	  if (h>0 && w>0){
    		this.width = w;
    		this.height = h;
  }else{
  	this.width = 0;
	this.height = 0;
  }
}
module.exports = Rectangle;