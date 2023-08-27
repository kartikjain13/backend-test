async function calc() {
    const equationTextarea = document.getElementById('eq');
    const resultSpan = document.getElementById('res');
   

    const equation = equationTextarea.value;

    const response = await fetch(`/calculate/${encodeURIComponent(equation)}`); 
    const data = await response.json();

    if (data.result !== undefined) {
        resultSpan.textContent = `${data.result}`;
    } else if (data.error) {
        resultSpan.textContent = `${data.error}`;
    }

    equationTextarea.value = '';
}