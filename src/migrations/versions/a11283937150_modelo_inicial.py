"""modelo inicial

Revision ID: a11283937150
Revises: 
Create Date: 2024-10-29 19:10:34.007299

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session  # Corrigir a importação

from models.product import Product  # Importa o modelo Product


# revision identifiers, used by Alembic.
revision = 'a11283937150'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.Column('order_number', sa.String(length=10), nullable=True),
    sa.Column('user_name', sa.String(length=100), nullable=True),
    sa.Column('user_email', sa.String(length=100), nullable=True),
    sa.Column('total_price', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('is_open', sa.Boolean(), nullable=True),
    sa.Column('address1', sa.String(length=255), nullable=True),
    sa.Column('address2', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('state', sa.String(length=100), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('zip_code', sa.String(length=20), nullable=True),
    sa.Column('mobile', sa.String(length=20), nullable=True),
    sa.Column('card_name', sa.String(length=100), nullable=True),
    sa.Column('card_number', sa.String(length=20), nullable=True),
    sa.Column('expiry_date', sa.String(length=5), nullable=True),
    sa.Column('cvv', sa.String(length=4), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('order_number'),
    sa.UniqueConstraint('uuid')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('short_description', sa.String(length=200), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


    # Inserir produtos após a criação da tabela
    bind = op.get_bind()  # Obter a conexão com o banco
    session = Session(bind=bind)  # Criar a sessão SQLAlchemy

  # Lista de produtos a serem adicionados
    products = [
        Product(
            name="Webcam Ultra HD 4K MX Brio",
            price=1299.00,
            description="A Logitech MX Brio é uma webcam de alta performance, ideal para streamers que buscam qualidade excepcional em vídeo. Com resolução 4K Ultra HD e tecnologia HDR, oferece imagens nítidas e cores vibrantes. Possui autofoco avançado e campo de visão ajustável, além de microfones estéreo embutidos, proporcionando áudio claro e sem ruídos. A MX Brio ainda conta com suporte para Windows Hello e Logitech Capture, facilitando o ajuste de configurações para streaming.",
            short_description="Estou apaixonado pelo kubernetes e pipelines ci/cd",
            image="product-1.jpg"
        ),
        Product(
            name="Elgato Stream Deck",
            price=1199.00,
            description="O Elgato Stream Deck é uma ferramenta essencial para criadores de conteúdo que desejam uma experiência de streaming dinâmica e profissional. Com 15 teclas LCD personalizáveis, o Stream Deck permite controle total das ações no streaming, facilitando comandos para transições, inserção de sons, mensagens no chat e muito mais. Ele é compatível com OBS, Twitch, YouTube e outras plataformas, tornando cada transmissão mais prática e interativa.",
            short_description="Controle suas streams com 15 teclas personalizáveis",
            image="product-2.jpg"
        ),
        Product(
            name="Galaxy Book4",
            price=4199.00,
            description="O Galaxy Book4 é o notebook ideal para streamers e criadores que priorizam mobilidade e desempenho. Com processadores de última geração e integração total com o ecossistema Samsung, ele facilita a troca de arquivos e permite o espelhamento de tela com dispositivos Galaxy. A tela Full HD e a bateria de longa duração tornam o Galaxy Book4 perfeito para transmissões ao vivo e edições de vídeo.",
            short_description="Notebook leve e potente com integração Samsung",
            image="product-3.jpg"
        ),
        Product(
            name="Notebook Dell XPS 13",
            price=8999.00,
            description="O Dell XPS 13 é um dos notebooks mais recomendados para streamers e criadores de conteúdo devido ao seu desempenho de ponta e design premium. Com uma tela infinita de alta resolução 4K, ele oferece uma experiência visual imersiva, perfeita para edições e transmissões. Equipado com processadores Intel Core i7 e armazenamento SSD, o XPS 13 combina velocidade e eficiência, ideal para multitarefa.",
            short_description="Notebook compacto com tela infinita 4K e desempenho premium",
            image="product-4.jpg"
        ),
        Product(
            name="JBL Tune 720BT",
            price=349.00,
            description="O JBL Tune 720BT é um fone de ouvido Bluetooth acessível e confortável, perfeito para quem busca boa qualidade de som com graves impactantes. Com até 50 horas de reprodução contínua, ele é ideal para sessões prolongadas de streaming ou edição de vídeos. Leve e fácil de ajustar, proporciona boa vedação contra ruídos externos.",
            short_description="Fone Bluetooth leve com graves intensos e longa bateria",
            image="product-5.jpg"
        ),
        Product(
            name="Smartphone Samsung Galaxy S22",
            price=4499.00,
            description="O Samsung Galaxy S22 é um dos smartphones mais avançados para criação de conteúdo móvel. Equipado com uma câmera principal de alta resolução e gravação em 8K, ele captura imagens e vídeos em qualidade profissional. Ideal para vloggers e streamers que gostam de transmitir de qualquer lugar.",
            short_description="Smartphone com câmera avançada e gravação em 8K",
            image="product-6.jpg"
        ),
        Product(
            name="Câmera EOS Rebel SL3",
            price=3999.00,
            description="A Canon EOS Rebel SL3 é uma câmera DSLR leve e compacta, ideal para streamers e vloggers que buscam alta qualidade de imagem sem comprometer a portabilidade. Com sensor de 24.1 MP e capacidade de gravação em 4K, oferece captura de detalhes impressionantes e cores vibrantes.",
            short_description="DSLR compacta com 24.1 MP e gravação em 4K",
            image="product-7.jpg"
        ),
        Product(
            name="Microfone Hollyland Lark M2 Duo",
            price=1399.00,
            description="O Hollyland Lark M2 Duo é um microfone de lapela sem fio que oferece áudio de qualidade para streamers e criadores de conteúdo. Com dois transmissores e um receptor, ele permite captação de áudio para entrevistas e transmissões em dupla, mantendo clareza e baixo ruído.",
            short_description="Microfone de lapela duplo com áudio cristalino e transmissão sem fio",
            image="product-8.jpg"
        ),
        Product(
            name="Microfone Condensador Blue Yeti",
            price=899.00,
            description="O Blue Yeti é um microfone condensador USB amplamente usado por streamers e podcasters devido à sua qualidade sonora e versatilidade. Oferecendo múltiplos padrões de captação, ele é perfeito para diferentes tipos de gravação, seja streaming, podcasting ou entrevistas.",
            short_description="Microfone condensador USB para gravações de alta qualidade",
            image="product-9.jpg"
        ),
    ]

    # Adicionar e fazer commit dos produtos na sessão
    session.bulk_save_objects(products)
    session.commit()
    session.close()  # Fechar a sessão


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_items')
    op.drop_table('products')
    op.drop_table('orders')
    # ### end Alembic commands ###
