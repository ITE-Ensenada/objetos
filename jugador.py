class Link(pygame.sprite.Sprite):
	def __init__(self, position):
		self.sheet = pygame.image.load('imagenes/link.png')
		self.sheet.set_clip(pygame.Rect(0, 0, 92, 106))
		self.image = self.sheet.subsurface(self.sheet.get_clip())
		self.rect = self.image.get_rect()
		self.rect.topleft = position 
		self.frame = 0
		self.rest = {0: (0, 0, 92, 106), 1: (92, 0, 92, 106), 2: (184, 0, 92, 106) }
		self.left_states = {0: (0, 522, 96, 92), 1:(92, 522, 96, 92), 2: (184, 522, 96, 92), 3:(276, 522, 96, 92), 4: (368, 522, 96, 92)} 
		self.right_states = {0: (0, 731, 96, 92), 1: (92, 731, 96, 92), 2: (184, 731, 96, 92), 3: (276, 731, 96, 92), 4: (368, 731, 96, 92)}
	
	def get_frame(self, frame_set):
		self.frame += 1
		if self.frame >(len(frame_set) - 1):
			self.frame = 0
		return frame_set(self.frame)

	def clip(self, clipped_rect):
		if type(clipped_rect) is dict:
			self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
		else:
			self.sheet.set_clip(pygame.Rect(clipped_rect))
			return clipped_rect

	def update(self, direction):
		if direction == 'left':
			self.clip(self.left_states)
			self.rect.x -= 5
		if direction == 'right':
			self.clip(self.right_states)
			self.rect.x += 5

		if direction == 'stand_left':
			self.clip(self.left_states[0])
		if direction == 'stand_right':
			self.clip(self.right_states[0])	

		self.image = self.sheet.subsurface(self.sheet.get_clip())

	def handle_event(self, event):
		if event.type == pygame.QUIT:
			game_over = True

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_a:
				self.update('left')
			if event.key == pygame.K_d:
				self.update('right')	

		if event.type == pygame.KEYUP:

			if event.key == pygame.K_a:
				self.update('stand_left')
			if event.key == pygame.K_d:
				self.update('stand_right')