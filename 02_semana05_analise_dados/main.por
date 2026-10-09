// Semana 05: validação de registros e tratamento de erros.
// Representação didática da lógica em Portugol.

programa {
    funcao logico email_valido(cadeia email) {
        retorne contem(email, "@")
    }

    funcao logico cpf_valido(cadeia cpf) {
        retorne comprimento(cpf) == 14
    }

    funcao inicio() {
        cadeia emails[4] = {"ana@email.com", "bruno.email.com", "carla@email.com", "diego@email.com"}
        cadeia cpfs[4] = {"123.456.789-09", "111.222.333-44", "987.654.321-00", "12345678909"}
        inteiro validos = 0
        inteiro i

        para (i = 0; i < 4; i++) {
            tente {
                se (email_valido(emails[i]) e cpf_valido(cpfs[i])) {
                    escreva("Registro ", i + 1, ": válido\n")
                    validos++
                } senao {
                    escreva("Registro ", i + 1, ": inválido\n")
                }
            } capture (cadeia erro) {
                escreva("Erro: ", erro, "\n")
            }
        }
        escreva("Total válido: ", validos, " de 4\n")
    }
}
