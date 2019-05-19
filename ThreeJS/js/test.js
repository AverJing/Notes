//相关变量
    var scene,
    camera, fieldOfView, aspectRatio, nearPlane, farPlane,
    renderer, container, cube;
    var HEIGHT, WIDTH;

    function createScene(){
        HEIGHT = window.innerHeight;
        WIDTH = window.innerWidth;
        scene = new THREE.Scene();
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
        camera.position.z = 5;
        renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        renderer.setSize(WIDTH, HEIGHT);
        //renderer.shadowMap.enabled = true;

        container = document.getElementById('world');
        container.appendChild(renderer.domElement);
    }

    function createCube(){
        var geometry = new THREE.BoxGeometry(1,1,1);
        var material = new THREE.MeshBasicMaterial({color:0x00ff00});
        cube = new THREE.Mesh(geometry, material);
        scene.add(cube);
    }

    function loop(){
        requestAnimationFrame(loop);
        renderer.render(scene, camera);       
    }

    function init(){
        createScene()
        createCube();
        loop()
    }

window.addEventListener('load', init, false);