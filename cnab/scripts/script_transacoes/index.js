// Iniciando a manipulação com DOM

const body = document.querySelector("body");
const divTable = document.getElementsByTagName("divTable");

let BASE_URL = "http://127.0.0.1:8000";

const table_generate = async () => {
  const return_data = await fetch(`${BASE_URL}/api/transacoes/`);
};
// table_generate();
