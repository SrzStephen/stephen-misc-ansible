import tensorflow as tf
from operator import itemgetter
tf.debugging.set_log_device_placement(True)


if __name__ == "__main__":
    if not tf.test.gpu_device_name() or not tf.test.is_built_with_gpu_support() or not tf.test.is_gpu_available():
        print(
            f"No GPU Found, only {tf.config.list_physical_devices()}, tf built {tf.test.is_built_with_gpu_support()} gpu available {tf.test.is_gpu_available()}")
        exit(1)
    else:
        with tf.device('/GPU:0'):
            a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
            b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
            c = tf.matmul(a, b)
        print(c)
        exit(0)
