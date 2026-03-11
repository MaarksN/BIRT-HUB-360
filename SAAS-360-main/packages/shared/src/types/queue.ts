export interface QueueMessage<T = any> {
  id: string;
  payload: T;
  timestamp: Date;
  retryCount: number;
}

export interface QueueAdapter {
  publish(topic: string, message: QueueMessage): Promise<void>;
  subscribe(topic: string, handler: (msg: QueueMessage) => Promise<void>): void;
}