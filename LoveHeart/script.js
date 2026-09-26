const container =
    document.getElementById("heart-container");


// =================================================
// SETTINGS
// =================================================

const WORDS_PER_LAYER = 45;

const LAYERS = 7;

const CENTER_X = 350;

const CENTER_Y = 300;


// Heart size

const HEART_SCALE_X = 17;

const HEART_SCALE_Y = 17;


// Animation speed

const SPEED = 0.0012;


// =================================================
// Store all words
// =================================================

const words = [];


// =================================================
// Heart equation
// =================================================

function heartX(t) {

    return 16 * Math.pow(Math.sin(t), 3);

}


function heartY(t) {

    return (
        13 * Math.cos(t)
        - 5 * Math.cos(2 * t)
        - 2 * Math.cos(3 * t)
        - Math.cos(4 * t)
    );

}


// =================================================
// Create multiple layers
// =================================================

for (let layer = 0; layer < LAYERS; layer++) {


    // Each layer has different distance
    // from the center line

    const layerOffset =
        (layer - (LAYERS - 1) / 2) * 7;


    for (
        let i = 0;
        i < WORDS_PER_LAYER;
        i++
    ) {


        const word =
            document.createElement("span");


        word.classList.add("love-word");


        word.innerText = "I love you";


        // Make some words brighter

        if (i % 13 === 0) {

            word.classList.add("bright");

        }


        // Make some words dimmer

        if (i % 7 === 0) {

            word.classList.add("dim");

        }


        container.appendChild(word);


        words.push({

            element: word,

            index: i,

            layer: layer,

            offset: layerOffset,

            phase:
                (i / WORDS_PER_LAYER)
                * Math.PI
                * 2

        });

    }

}


// =================================================
// Animation time
// =================================================

let time = 0;


// =================================================
// Animation
// =================================================

function animate() {


    time += SPEED;


    words.forEach(item => {


        // -----------------------------------------
        // Position around heart
        // -----------------------------------------

        const t =
            time + item.phase;


        // -----------------------------------------
        // Heart position
        // -----------------------------------------

        let x =
            heartX(t)
            * HEART_SCALE_X;


        let y =
            heartY(t)
            * HEART_SCALE_Y;


        // -----------------------------------------
        // Create multiple heart layers
        // -----------------------------------------

        const length =
            Math.sqrt(x * x + y * y);


        if (length !== 0) {

            x +=
                (x / length)
                * item.offset;

            y +=
                (y / length)
                * item.offset;

        }


        // -----------------------------------------
        // Screen coordinates
        // -----------------------------------------

        const screenX =
            CENTER_X + x;


        const screenY =
            CENTER_Y - y;


        // -----------------------------------------
        // Direction of movement
        // -----------------------------------------

        const nextT =
            t + 0.01;


        const nextX =
            heartX(nextT)
            * HEART_SCALE_X;


        const nextY =
            heartY(nextT)
            * HEART_SCALE_Y;


        const angle =
            Math.atan2(
                -(nextY - y),
                nextX - x
            )
            * 180
            / Math.PI;


        // -----------------------------------------
        // Apply position
        // -----------------------------------------

        item.element.style.left =
            `${screenX}px`;


        item.element.style.top =
            `${screenY}px`;


        // -----------------------------------------
        // Rotate text with heart
        // -----------------------------------------

        item.element.style.transform =
            `
            translate(-50%, -50%)
            rotate(${angle}deg)
            `;

    });


    requestAnimationFrame(animate);

}


// Start

animate();