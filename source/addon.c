#ifndef ADDON
#define ADDON

typedef unsigned int uint;
typedef unsigned long Color;

typedef struct {
	int x;
	int y;
} Vector2;

typedef struct {
	int left;
	int top;
	int right;
	int bottom;
} Rectangle;

Vector2 newVector2(int x, int y){
	Vector2 vec;
	vec.x = x;
	vec.y = y;
	return vec;
}

Rectangle newRectangle(int x, int y,uint right, uint bottom){
	Rectangle rect;
	rect.left = x;
	rect.top = y;
	rect.right = rect.left + right;
	rect.bottom = rect.top + bottom;
	return rect;
}

/**
 * @brief If the 'Vector' is inside a 'Rectangle'
 * 
 * @param vector Vector2 point you wish to know if it is in a Rectangle
 * @param rect the target Rectangle
 * @return true or
 * @return false 
 */
bool isVectorInBox(Vector2 vector, Rectangle rect){
	if( vector.x < rect.right && \
		vector.x > rect.left && \
		vector.y < rect.bottom && \
		vector.y > rect.top) {return true;}
	else{return false;}
}

#endif