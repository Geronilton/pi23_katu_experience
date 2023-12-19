CREATE DATABASE IF NOT EXISTS BD_katu; 


USE BD_katu; 

CREATE TABLE IF NOT EXISTS Usuario ( 

  idUsuario INT NOT NULL AUTO_INCREMENT, 
  nome VARCHAR(60) NOT NULL, 
  cpf VARCHAR(11) NOT NULL, 
  telefone VARCHAR(11) NOT NULL, 
  email VARCHAR(50) NOT NULL, 
  PRIMARY KEY (idUsuario) 
); 

  

CREATE TABLE IF NOT EXISTS Agendamento ( 

  idagendamento INT NOT NULL AUTO_INCREMENT, 
  data_registro DATE NOT NULL, 
  data_proposta DATE NOT NULL, 
  data_confirmacao DATE NOT NULL, 
  Qtd_pessoas INT NOT NULL, 
  Passeio_idPasseio INT NOT NULL, 
  Usuario_idUsuario INT NOT NULL, 
  PRIMARY KEY (idagendamento), 
  FOREIGN KEY (Usuario_idUsuario) REFERENCES Usuario(idUsuario), 
  FOREIGN KEY (Passeio_idPasseio) REFERENCES Usuario(idUsuario)
); 

  

CREATE TABLE IF NOT EXISTS Passeio ( 

  idPasseio INT NOT NULL AUTO_INCREMENT, 
  titulo VARCHAR(30) NOT NULL, 
  descricao VARCHAR(200) NOT NULL, 
  valor DOUBLE NOT NULL, 
  PRIMARY KEY (idPasseio)
 ); 