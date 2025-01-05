let quantidade_vitorias = 78;
let quantidade_derrotas = 24;
calcular_ranking(quantidade_vitorias, quantidade_derrotas)

function calcular_ranking(quantidade_vitorias, quantidade_derrotas) {
    let saldo_rankeadas = quantidade_vitorias - quantidade_derrotas;
    let nivel_heroi;

    if (saldo_rankeadas <= 10) {
        nivel_heroi = 'Ferro';
    }
    else if (saldo_rankeadas > 10 && saldo_rankeadas <= 20) {
        nivel_heroi = 'Bronze';
    }
    else if (saldo_rankeadas > 20 && saldo_rankeadas <= 50) {
        nivel_heroi = 'Prata';
    }
    else if (saldo_rankeadas > 50 && saldo_rankeadas <= 80) {
        nivel_heroi = 'Ouro';
    }
    else if (saldo_rankeadas > 80 && saldo_rankeadas <= 90) {
        nivel_heroi = 'Diamante';
    }
    else if (saldo_rankeadas > 91 && saldo_rankeadas <= 100) {
        nivel_heroi = 'Lendário';
    }

    return console.log(`O Herói tem saldo de ${saldo_rankeadas} está no nível de ${nivel_heroi}`);
}
