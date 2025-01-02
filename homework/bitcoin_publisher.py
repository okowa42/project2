import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import requests
import time

class BitcoinPublisher(Node):
    def __init__(self):
        super().__init__('bitcoin_publisher')
        self.publisher_ = self.create_publisher(Float32, 'bitcoin_price', 10)
        self.timer = self.create_timer(10.0, self.timer_callback)  # 30秒ごとにコールバックを呼び出す

    def timer_callback(self):
        try:
            # CoinGecko APIからビットコインの価格を取得
            url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
            response = requests.get(url)
            response.raise_for_status()  # HTTPエラーをキャッチ
            data = response.json()

            # ビットコインの価格を取得し、floatに変換
            bitcoin_price = float(data['bitcoin']['usd'])

            # トピックにビットコインの価格をパブリッシュ
            msg = Float32()
            msg.data = bitcoin_price
            self.publisher_.publish(msg)
            self.get_logger().info(f"Bitcoin price: {bitcoin_price} USD")

        except requests.exceptions.HTTPError as e:
            # レートリミットエラー対応
            if e.response.status_code == 429:
                self.get_logger().error("Rate limit exceeded. Retrying after delay...")
                time.sleep(60)  # 60秒待機して再試行
            else:
                self.get_logger().error(f"HTTP error occurred: {e}")

        except (requests.RequestException, KeyError, ValueError) as e:
            # その他のエラーをログに記録
            self.get_logger().error(f"Failed to fetch Bitcoin price: {e}")

def main(args=None):
    rclpy.init(args=args)

    bitcoin_publisher = BitcoinPublisher()

    rclpy.spin(bitcoin_publisher)

    bitcoin_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

