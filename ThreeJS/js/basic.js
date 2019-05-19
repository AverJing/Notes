//相关变量
var scene,
    camera, fieldOfView, aspectRatio, nearPlane, farPlane,
    renderer, container;
var HEIGHT, WIDTH;

var fireworks = [];
var timerTotal = 20, timerTick = 0;

function createScreen(){
    HEIGHT = window.innerHeight;
    WIDTH = window.innerWidth;

    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x000000);
    aspectRatio = WIDTH / HEIGHT;
    fieldOfView = 60;
    nearPlane = 0.1;
    farPlane = 1000;
    camera = new THREE.PerspectiveCamera(
        fieldOfView,
        aspectRatio,
        nearPlane,
        farPlane
        );
    //scene.fog = new THREE.Fog(0xf7d9aa, 100,950);
    camera.position.set(0,0,20);

    renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(WIDTH, HEIGHT);
    //renderer.shadowMap.enabled = true;
  
    container = document.getElementById('world');
    container.appendChild(renderer.domElement);

    window.addEventListener('resize', handleWindowResize, false);
}

function handleWindowResize(){
    HEIGHT = window.innerHeight;
    WIDTH = window.innerWidth;

    renderer.setSize(WIDTH, HEIGHT);
    camera.aspect = WIDTH/HEIGHT;
    camera.updateProjectionMatrix();
}

//工具函数
function random(min, max){
    return Math.random() * (max - min) + min;
}

function calculateDistance( p1x, p1y, p2x, p2y ) {
	var xDistance = p1x - p2x,
			yDistance = p1y - p2y;
	return Math.sqrt( Math.pow( xDistance, 2 ) + Math.pow( yDistance, 2 ) );
}

var Line = function(s, e){
    var material = new THREE.LineBasicMaterial({
        color: 0xffffff,
        linewidth: 1
    });
    
    var geometry = new THREE.Geometry();
    geometry.vertices.push(
        s,
        e
    );
    this.line = new THREE.LineSegments(geometry, material);
}

function Firework(sx, sy, tx, ty){
	//起点坐标
	this.sx = sx;
	this.sy = sy;
	//终点坐标
	this.tx = tx;
	this.ty = ty;
	//起点和终点的距离
	this.distanceToTarget = calculateDistance( sx, sy, tx, ty );
	this.distanceTraveled = 0;
	this.speed = 1;
	this.acceleration = 1.05;
	this.brightness = random( 50, 70 );
	//辐射半径
    this.targetRadius = 1;
    this.line = new Line(new THREE.Vector3(sx, sy, 0), new THREE.Vector3(sx, sy, 0));
    scene.add(this.line.line);
}

Firework.prototype.update = function(){	
	// cycle the circle target indicator radius
	if( this.targetRadius < 8 ) {
		this.targetRadius += 0.3;
	} else {
		this.targetRadius = 1;
	}
	
	// speed up the firework
    this.speed *= this.acceleration;
    
	// how far will the firework have traveled with velocities applied?
	this.distanceTraveled = calculateDistance( this.sx, this.sy, this.line.line.geometry.vertices[1].x, this.line.line.geometry.vertices[1].y + this.speed );
	
	// if the distance traveled, including velocities, is greater than the initial distance to the target, then the target has been reached
	if( this.distanceTraveled >= this.distanceToTarget ) {
		//createParticles( this.tx, this.ty );
		// remove the firework, use the index passed into the update function to determine which to remove
        fireworks.splice( 0, 1 );
        scene.remove(this.line.line);
	} else {
        // target not reached, keep traveling
        this.line.line.geometry.vertices[0].y = (this.line.line.geometry.vertices[1].y);
        this.line.line.geometry.vertices[1].y += this.speed;
        this.line.line.geometry.verticesNeedUpdate = true;
	}
}

var Cube = function(){
    var geometry = new THREE.BoxGeometry(10,10,10);
    var material = new THREE.MeshBasicMaterial({color:0x00ff00});
    this.mesh = new THREE.Mesh(geometry, material);
}

function createCube(){
    cube = new Cube();
    scene.add(cube.mesh);
}

var tmpLine;
function createLine(){
    var tmpH = HEIGHT/2, tmpW = WIDTH/2;
    var s = new THREE.Vector3(0, 0, 0);
    var e = new THREE.Vector3(0, 0.5, 0);
    tmpLine = new Line(s, e);
    scene.add(tmpLine.line);
}

var time = 0;

function loop(){
    requestAnimationFrame(loop);

    var i = fireworks.length;
	while( i-- ) {
        fireworks[ i ].update();
    }

    renderer.render(scene, camera);
    
    if( timerTick >= timerTotal ) {
		var ox = random( -5, 5);
		var oy = random( -5, 5);
		fireworks.push( new Firework( ox, -12 , ox, oy ) );
		timerTick = 0;
	} else {
		timerTick++;
	}
}

function init(){
    createScreen();
    //createCube();
    //createLine();
    loop();
}

window.addEventListener('load', init, false);