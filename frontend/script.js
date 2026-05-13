async function predictPrice() {

    // Récupère la valeur du champ
    const surface = document.getElementById("surface").value;

    // URL de ton API
    const API_URL =
        "https://housing-prices-8k2j.onrender.com/predict";

    try {

        // Envoi de la requête POST
        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                surface: Number(surface)
            })
        });

        // Conversion JSON
        const data = await response.json();
        console.log(data)

        // Affichage résultat
        document.getElementById("result").innerText =
            "Prix estimé : " +
            data.prediction +
            " €";

    } catch (error) {

        console.error(error);

        document.getElementById("result").innerText =
            "Erreur lors de la prédiction";
    }
}