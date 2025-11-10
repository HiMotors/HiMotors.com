CREATE TABLE Cliente (
  id_cliente INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  cpf CHAR(11) UNIQUE NOT NULL,
  telefone VARCHAR(20),
  email VARCHAR(100)
);

CREATE TABLE Funcionario (
  id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  cpf CHAR(11) UNIQUE NOT NULL,
  cargo VARCHAR(50)
);

CREATE TABLE Categoria (
  id_categoria INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(50) NOT NULL,
  descricao TEXT,
  diaria DECIMAL(10,2) NOT NULL
);

CREATE TABLE Carro (
  id_carro INT AUTO_INCREMENT PRIMARY KEY,
  modelo VARCHAR(50) NOT NULL,
  marca VARCHAR(50) NOT NULL,
  placa CHAR(7) UNIQUE NOT NULL,
  ano INT NOT NULL,
  status ENUM('disponível','alugado','manutenção') DEFAULT 'disponível',
  id_categoria INT,
  FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);

CREATE TABLE Locacao (
  id_locacao INT AUTO_INCREMENT PRIMARY KEY,
  data_inicio DATE NOT NULL,
  data_fim DATE,
  km_inicial INT,
  km_final INT,
  valor_total DECIMAL(10,2),
  id_cliente INT,
  id_carro INT,
  id_funcionario INT,
  FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),
  FOREIGN KEY (id_carro) REFERENCES Carro(id_carro),
  FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
);

CREATE TABLE Pagamento (
  id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
  data_pagamento DATE NOT NULL,
  valor DECIMAL(10,2) NOT NULL,
  forma_pagamento ENUM('dinheiro','cartão','pix','transferência'),
  id_locacao INT,
  FOREIGN KEY (id_locacao) REFERENCES Locacao(id_locacao)
);
