import socket

HOST = '127.0.0.1'
# HOST = '211.104.118.60'
PORT = 10901

def socket_response(msg):
    # 로컬은 127.0.0.1의 ip로 접속한다
# port는 위 서버에서 설정한 9999로 접속을 한다

# 소켓 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect 함수로 접속
    client_socket.connect((HOST, PORT))

    # 메시지를 바이너리(byte) 형식으로 변환
    data = msg.encode();
    # 메시지 길이를 구한다
    length = len(data);
    # server로 little 형식으로 데이터 길이를 전송한다s
    client_socket.sendall(length.to_bytes(4, byteorder="little"));
    # 데이터 전송
    client_socket.sendall(data);

    # server로부터 전송받을 데이터 길이를 받는다
    data = client_socket.recv(1024);
    # 데이터 길이는 little 엔디언 형식으로 int를 변환
    length = int.from_bytes(data, "little");
    # 데이터 길이를 받는다
    data = client_socket.recv(length);
    # 데이터를 수신한다
    msg = data.decode();
    # 데이터를 출력
    print('Received from : ', msg);

    client_socket.close();
    return msg
